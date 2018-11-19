import csv, reportlab, io, json
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from random import choices
from django.contrib.auth.decorators import permission_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from exam_writer.models import CustomUser
from .models import Subject, SubjectCategories, TermSession, Question, ExamRecord
from examination.utils import render_to_pdf

# Views.
def home_view(request):
	#user_info = request.GET.get('username')
	subjects = Subject.objects.all()
	return render(request, "exam/index.html", {"subjects": subjects})

def index_view(request, id):
	user_key = 'ayua' #request.GET.get('public_key')
	terms = TermSession.objects.all()
	subjects = Subject.objects.all()
	cats = SubjectCategories.objects.all()
	#queryset = get_object_or_404(Question, subject_id=subject, id=id)
	all_q = Question.objects.filter(subject_id=id).filter(published=True)
	tot_num = len(all_q)
	
	print("correct answers")
	queryset = all_q #choices(all_q)

	if request.method == "POST":
		#print(request.body)
		exam_subject = id #request.GET.get(id)
		val = request.body.decode('utf-8')
		#print(' --- for val variable ---- ')
		#print(val)
		answers = str(val)

		options=[]
		answer=[]
		corrct = []
		final = []

		for qu in all_q:
			corrct.append(qu.correct_ans)

		for opt in answers.split('&',):
			#print(opt[-6])
			#numbers=num.split('&')
			#print(num[-1])
			options.append(opt[-6])
		#print(' end of options ')

		for ans in answers.split('&'):
			#print(ans[-1])
			answer.append(ans[-1])
			options = str(options)
		print("commment")
		# TRy to compare choices with correct answers
		print(corrct, " = ", answer)

		if len(corrct) == len(answer):
			for i in range(len(corrct)):
				if corrct[i] == answer[i]:
					final.append(1)
				else:
					final.append(0)
		final_correct = final.count(1)
		print("all the value")
		print(final_correct)
		attempt = len(final)
		print(attempt, "NUmbers of attempts")
		print(final)
		remark = ""
		print("The returns")
		if final_correct == len(final):
			remark = "Excellent"
			print(remark)
		elif final_correct < len(final) and final_correct > len(final) / 2:
			remark = "Very good performance"
			print(remark)
		elif final_correct != len(final) and final_correct <= len(final) / 2:
			remark = "Below average, Try again"
			print(remark)
		else:
			print("You did not meet up the Score")
		#print(remark, "#######")
		try:
			ExamRecord.objects.create(
					exam_subject = exam_subject,
					user_key = user_key,
					attempt = attempt,
					score = final_correct,
					remark = remark,
				) #  messages.success(request, 'Su
			print('Successfully saved.!')
			return redirect('/')
		except Exception as e:
			print(str(e))
		#print('Yess.! Its a goaaal.')
	context = {
		'total_quest': tot_num,
		'questions': queryset,
		'subjects': subjects,
		'cats': cats,
		'terms': terms
	}
	return render(request, "exam/home.html", context)

### Exam result
def userResult(request):
	#subject = Question.objects.filter(id=id)
	available_ch = Question.objects.filter(subject_id = 1)
	queryset = ExamRecord.objects.filter(user_key='angel')

	# correct_choic = []
	# user_choic = []
	# final = dict()

	# for ava in available_ch:
	# 	print(ava.id)
	# 	correct_choic.append(ava.correct_ans)
	# 	print(ava.correct_ans)
	# #print(available_ch.correct_ans)
	# print("available answers")
	# #queryset.split(' ')

	# for query in queryset:
	# 	opt = query.attempt
	# 	answ = query.score
	# 	commment = query.remark

	# 	if answ != '"' and answ != '[' and answ != ']':
	# 		x = answ.replace(",", "")
	# 		if 'A' in x or 'B' in x or 'C' in x or 'D' in x:
	# 			user_choic.append(x)
	# 			print(x)
	# 		print("Hey success")

	# #print(correct_choic, ' = ', user_choic[0])
	# print("End view loop")


	context = {
			'queryset': queryset
	}
	return render(request, "output/checker.html", context)

def examView(request):
	user_info = request.GET.get('public_key')
	subjects = Subject.objects.all()
	print(str(user_info))
	if user_info != None:
		return render(request, "exam/index.html", {"subjects": subjects})
	else:
		return django.http.HttpResponseBadRequest("Sorry request is unrecorgnise")
	return render(request, "exam/index.html", {"subjects": subjects})

## For question Upload
def questionFile(request, *args, **kwargs):
	terms = TermSession.objects.all()
	subjects = Subject.objects.all()
	category = SubjectCategories.objects.all()
	context = {
		'terms': terms,
		'subjects': subjects,
		'category': category
	}
	if request.method == "POST":
		# post CSV to database
		term = request.POST.get('term')
		subject = request.POST.get('subject')
		category = request.POST.get('category')
		question = request.POST.get('question')
		option_a = request.POST.get('option_a')
		option_b = request.POST.get('option_b')
		option_c = request.POST.get('option_c')
		option_d = request.POST.get('option_d')
		option_e = request.POST.get('option_e')
		
		Question.objects.create(
				term_question_id = term,  #TermSession.objects.get(id=term),
				subject_id_id = subject,  #Subject.objects.get(id=subject),
				category_id_id = category,
				question = question,
				option_a = option_a,
				option_b = option_b,
				option_c = option_c,
				option_d = option_d,
				correct_ans = option_e
			)
		return redirect('/', messages.success(request, 'Successfully added question.'))
		
	else:
		return render(request, "exam/questions_create.html", context)

@permission_required('admin.can_add_log_entry')
def subjectCreate(request):
	terms = TermSession.objects.all()
	cats = SubjectCategories.objects.all()
	context = {
		'terms': terms,
		'cats': cats
	}
	if request.method == "POST":
		name = request.POST.get('name')
		code = request.POST.get('code')
		subject_term = request.POST.get('subject_term')
		category = request.POST.get('category')

		Subject.objects.create(
			name = name,
			code = code,
			subject_term_id = subject_term,
			category_id_id = category
			)
		return redirect('/', messages.success(request, 'Successfully added subject.'))
	else:
	 	return render(request, "exam/admCreateSub.html", context)

@permission_required('admin.can_add_log_entry')
def questionCsvUpload(request):
	terms = TermSession.objects.all()
	subjects = Subject.objects.all()
	category = SubjectCategories.objects.all()
	order = 'CSV sholud be:--> question, option_a, option_b, option_c, option_d, option_e'

	if request.method == "POST":
		term = request.POST.get('term')
		subject = request.POST.get('subject')
		category = request.POST.get('category')
		csv_file = request.FILES['file']

		if not csv_file.name.endswith('.csv'):
			messages.error(request, "This file type is not supported")

		data_set = csv_file.read().decode('UTF-8')

		io_string = io.StringIO(data_set)

		next(io_string)
		for column in csv.reader(io_string, delimiter=',', quotechar="|"):
			_, created = Question.objects.update_or_create(
					term_question_id = term,
					subject_id_id = subject,
					category_id_id = category,
					question = column[0],
					option_a = column[1],
					option_b = column[2],
					option_c = column[3],
					option_d = column[4],
					correct_ans = column[5]
			)

		context = {}
		return render(request, "exam/questionCsvUpload.html", context)
	else:
		context = {
			'order': order,
			'terms': terms,
			'subjects': subjects,
			'category': category
		}
		return render(request, "exam/questionCsvUpload.html", context)

def result_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    # Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
	name = 'Samson'
	score = 50
	p.drawString(200, 200, name)

    # Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

### Trying 
from django.template.loader import get_template
from datetime import date

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/all_result.html')
        available_ch = Question.objects.filter(subject_id = 1)
        queryset = ExamRecord.objects.filter(user_key='ayua')
        subject = ""
        for sub in available_ch:
        	subject = sub.subject_id

        context = {
            'today': date.today(),
            "queryset": queryset,
            "subject": subject,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/all_result.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "HiH_result%s.pdf" %("6543789")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
