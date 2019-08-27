const getSavedList = function () {
    const todoJSON = localStorage.getItem("todoList");

    if (todoJSON !== null) {
        return JSON.parse(todoJSON);
    } else {
        return [];
    }
};

const saveList = function (todoList) {
    localStorage.setItem("todoList", JSON.stringify(todoList));
};

const renderItems = function (todoList, filters) {
    const filteredItems = todoList.filter(function (item) {
        const searchMatch = item.text.toLowerCase().includes(filters.searchText.toLowerCase());
        const hideMatch = !filters.hideComplete || !item.completed;
        return searchMatch && hideMatch;
    });

    document.querySelector("#todo-list").innerHTML = "";

    const summary = generateSummaryDOM(filteredItems);
    document.querySelector("#todo-list").appendChild(summary);

    filteredItems.forEach(function (item) {
        const itemElement = generateTodoDOM(item);
        document.querySelector("#todo-list").appendChild(itemElement);
    });
};

const generateTodoDOM = function (item) {
    const itemElement = document.createElement("p");
    itemElement.textContent = item.text;
    return itemElement;
};

const generateSummaryDOM = function (filteredItems) {
    const summary = document.createElement("h2");
    summary.textContent = `You have ${filteredItems.length} things left to do:`;
    return summary;
};