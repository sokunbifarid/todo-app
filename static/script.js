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
	document.getElementById("add_todo").className = "hidden popup";
	console.log("closed add todo popup");
}

function openModifyTodoPopup(id){
	focused_todo_id = id
	closeAllTodoPopup();
	document.getElementById("modify_todo").className = "visible";
	populate_modify_todo_popup();
	console.log("open modify popup");
}



function populate_modify_todo_popup(){
	let population_id = 0
	for (let i=0; i<todo_data.length; i++){
		if (todo_data.at(i).at(0) === focused_todo_id){
			population_id = i;
			break;
		}
	}
	let s_n = todo_data.at(population_id);
	console.log(todo_data.at(0));
	let todo_name = todo_data.at(population_id).at(2);
	let category = todo_data.at(population_id).at(3);
	let description = todo_data.at(population_id).at(4);
	document.getElementById("modify_todo_name").value = todo_name;
	document.getElementById("modify_todo_category").value = category;
	document.getElementById("modify_todo_description").value = description;
}

function closeModifyTodoPopup(){
	document.getElementById("modify_todo").className = "hidden";
	console.log("close modify popup");
}

function openDeleteTodoPopup(id){
	focused_todo_id = id;
	closeAllTodoPopup();
	document.getElementById("delete_todo").className = "visible";
	populate_delete_todo_popup();
	console.log("open delete popup");
}

function populate_delete_todo_popup(){
	let population_id = 0
	for (let i=0; i<todo_data.length; i++){
		if (todo_data.at(i).at(0) === focused_todo_id){
			populateion_id = i;
			break;
		}
	}
	let s_n = todo_data.at(population_id);
	console.log(todo_data.at(0));
	let todo_name = todo_data.at(population_id).at(2);
	let category = todo_data.at(population_id).at(3);
	let description = todo_data.at(population_id).at(4);
	document.getElementById("delete_todo_name").innerHTML = todo_name;
	document.getElementById("delete_todo_category").innerHTML = category;
	document.getElementById("delete_todo_description").innerHTML = description;
}

function closeDeleteTodoPopup(){
	document.getElementById("delete_todo").className = "hidden";
	console.log("close delete popup");
}

function confirmModify(){
	console.log("confirm modify function call");
	let todo_name = document.getElementById("modify_todo_name").value;
	let category = document.getElementById("modify_todo_category").value;
	let description = document.getElementById("modify_todo_description").value;
	fetch("/modify/" + focused_todo_id.toString() + "/" + todo_name + "/" + category + "/" + description, {method:"PUT"})
		.then(response =>{
			window.location.href="/";
		});
	focused_todo_id = 0;
	console.log("function confirm modify called");
}

function confirmDelete(){
	fetch("/delete/" + focused_todo_id.toString(), {method:"DELETE"})
		.then(response =>{
			window.location.href="/";
		});
	focused_todo_id = 0;
	console.log("function confirm delete called");
}

function closeAllTodoPopup(){
	closeAddTodoPopup();
	closeModifyTodoPopup();
	closeDeleteTodoPopup();
}

function logOut(){
	fetch("/logout").then(response =>{
		window.location.href="/";
	});
}

function goHome(){
	window.location.href="/";
}

function goLogin(){
	window.location.href = "/login";
}

function goRegister(){
	window.location.href = "/register";
}