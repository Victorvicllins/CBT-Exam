var Total_questions = document.getElementsByClassName('options');
var buttons = [];
var value_loop = 0;

for (i = 0; i < Total_questions.length / 4; i++){
	holder = [];
	for (j = 0; j < 4; j++){
		Total_questions[j + value_loop].id = `opt_${j + value_loop + 1}`
		holder.push(Total_questions[j + value_loop].id);
	}
	buttons[i] = holder;
	value_loop = value_loop + 4;
}
/*console.log(buttons);*/
var option_selected = {};
var page = 0;
var Question_page = document.getElementsByClassName("question");

for(i = 0; i < Question_page.length; i++){
	navs = document.getElementsByClassName('btn-group')[i].getElementsByClassName("btn")[i];
	navs.classList.add('active');
}

function options(options, Q_No, opt, number, num){
	unselected = []
	num = buttons[number][num]
	checkers(options, Q_No, opt, number, num);
}

function checkers(options, Q_No, opt, number, num){
	val = num;
	choice = document.getElementById(val);
	for (i = 0; i <= buttons[number].length - 1; i++) {
		if (buttons[number][i] == val){
			continue;
		}
		else {
			unselected.push(buttons[number][i]);
		}
	}
	for (i = 0; i < unselected.length; i++){
		if (document.getElementById(unselected[i]).classList.length > 0){
			document.getElementById(unselected[i]).classList.remove('select-opt');
		}
	}
	choice.classList.add("select-opt");
	option_selected[Q_No] = opt;
}

function quick_jump(val){
	val = val - 1;
	for (i = 0; i < Question_page.length; i++) {
		if (val == i){
			Question_page[val].style.display = 'block';
			page = val;
		}
		else{
			Question_page[i].style.display = 'none';
		}
	}
}
function pagination(page_nav, page_on){
	if (page_nav == "next"){
		if (page < Question_page.length - 1){
			Question_page[page].style.display = 'none';
			Question_page[page + 1].style.display = 'block';
			page++;
		}
	}
	else {
		if (page !== 0){
			Question_page[page].style.display = 'none';
			Question_page[page - 1].style.display = 'block';
			page--;	
		}
	}
}

