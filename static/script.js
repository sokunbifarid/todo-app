const datas = {{ data | tojson }};
console.log(datas)

function openAddTodoPopup(){
	closeAllTodoPopup();
	document.getElementById("add_todo").className = "visible";
	console.log("opened add todo popup");
}

function closeAddTodoPopup(){
	document.getElementById("add_todo").className = "hidden";
	console.log("closed add todo popup");
}

function openModifyTodoPopup(){
	closeAllTodoPopup();
	document.getElementById("modify_todo").className = "visible";
	console.log("open modify popup");
}

function closeModifyTodoPopup(){
	document.getElementById("modify_todo").className = "hidden";
	console.log("close modify popup");
}

function openDeleteTodoPopup(){
	closeAllTodoPopup();
	document.getElementById("delete_todo").className = "visible";
	console.log("open delete popup");
}

function closeDeleteTodoPopup(){
	document.getElementById("delete_todo").className = "hidden";
	console.log("close delete popup");
}

function confirmDelete(id){
	window.location.href="/index";
	console.log("function called");
}

function closeAllTodoPopup(){
	closeAddTodoPopup();
	closeModifyTodoPopup();
	closeDeleteTodoPopup();
}
