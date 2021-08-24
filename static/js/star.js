let score = document.getElementsByClassName('bookAvgscore')
const onestar = "★"

for (i=0; i<8; i++) {
    for (j=0; j<6; j++)
    if (score[i].innerText == j) {
        score[i].innerText = "★".repeat(j)
    }
}