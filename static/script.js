
//document.addEventListener("DOMContentLoaded", function()
//	{
//		const datas = {{ data | tojson | safe}};
//		console.log(datas)
//	}

let todo_data = [];
let focused_todo_id = 0;

fetch("/get_todo_list")
	.then(response => response.json())
	.then(data => {
		todo_data = data;
		console.log(todo_data);
	});

function openAddTodoPopup(){
	closeAllTodoPopup();
	document.getElementById("add_todo").className = "visible";
	console.log("opened add todo popup");
}

function closeAddTodoPopup(){
	document.getElementById("add_todo").className = "hidden";
	console.log("closed add todo popup");
}

function openModifyTodoPopup(id){
	focused_todo_id = id
	closeAllTodoPopup();
	document.getElementById("modify_todo").className = "visible";
	console.log("open modify popup");
}

function closeModifyTodoPopup(){
	document.getElementById("modify_todo").className = "hidden";
	console.log("close modify popup");
}

function openDeleteTodoPopup(id){
	focused_todo_id = id
	closeAllTodoPopup();
	document.getElementById("delete_todo").className = "visible";
	console.log("open delete popup");
}

function closeDeleteTodoPopup(){
	document.getElementById("delete_todo").className = "hidden";
	console.log("close delete popup");
}

function confirmModify(){
	window.location.href="/modify/" + str(focused_todo_id);
	focused_todo_id = 0
	console.log("function confirm modify called");
}

function confirmDelete(){
	window.location.href="/delete/" + focused_todo_id.toString();
	focused_todo_id = 0
	console.log("function confirm delete called");
}

function closeAllTodoPopup(){
	closeAddTodoPopup();
	closeModifyTodoPopup();
	closeDeleteTodoPopup();
}
