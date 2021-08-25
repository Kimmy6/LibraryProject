let historyStar = document.getElementsByClassName('historyAvgscore');

if (historyStar !== null) {
    let counter = historyStar.length;
    for (i=0;i<counter;i++) {
        for (j=0; j<6; j++)
            if (historyStar[i].innerText == j) {
            historyStar[i].innerText = "★".repeat(j) + "☆".repeat(5-j)
        }
    }
}