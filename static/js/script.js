// Toggle social links container
$("#social-links-button").click(function () {
    $("#social-links").toggle("fade", 200)
})


// Sets the width of textareas depending on screen size 
if ($(window).width() >= 768) {
    $(document).ready(function () {
        $("textarea").attr({
            "rows": "10",
            "cols": "55"
        });
    });
} else if ($(window).width() >= 576) {
    $(document).ready(function () {
        $("textarea").attr({
            "rows": "8",
            "cols": "50"
        });
    });
} else if ($(window).width() >= 400) {
    $(document).ready(function () {
        $("textarea").attr({
            "rows": "5",
            "cols": "35"
        });
    });
} else {
    $(document).ready(function () {
        $("textarea").attr({
            "rows": "5",
            "cols": "30"
        });
    });
}


// Auto increment of the year in footer

const copyrightYearRef = document.querySelector('#copyright-year')

const getFullYear = () => {
    let year = new Date().getFullYear();
    copyrightYearRef.innerHTML = year;
}

getFullYear()
