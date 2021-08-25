let bannapStar = document.getElementsByClassName('bannapAvgscore');

if (bannapStar !== null) {
    let counter = bannapStar.length;
    for (i=0;i<counter;i++) {
        for (j=0; j<6; j++)
            if (bannapStar[i].innerText == j) {
            bannapStar[i].innerText = "★".repeat(j) + "☆".repeat(5-j)
        }
    }
}