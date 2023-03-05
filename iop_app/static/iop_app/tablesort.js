/**
*Sorts a HTML table
*
*@param {HTMLTableElement}
*@param {number}
*@param {boolean}
*/

function sortTableByColumn(table, column, asc=true){
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    //sortowanie każdego rzędu
    const sortedRows = rows.sort((a, b) => {
        const aColText = a.querySelector(`td:nth-child(${ column + 1})`).textContent.trim();
        const bColText = b.querySelector(`td:nth-child(${ column + 1})`).textContent.trim();
        const aNum = parseInt(aColText);
        const bNum = parseInt(bColText);

    return (aNum - bNum) > 0 ? (1 * dirModifier) : (-1 * dirModifier);
  });

    // usuwa istniejące table rows z tabeli
    while(tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    };

    // dodaje table rows posortowane
    tBody.append(...sortedRows);

    // pamięta jak columny są posortowane - obecnie
    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-desc", !asc);
}

document.querySelectorAll(".table th").forEach(headerCell => {
    headerCell.addEventListener("click", () => {
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        const currentIsAscending = headerCell.classList.contains("th-sort-asc");

        sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
    });
});

