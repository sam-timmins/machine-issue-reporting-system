// Toggle social links container
$("#social-links-button").click(function () {
    $("#social-links").toggle("fade", 200)
})


// Toggle search bar container
$("#searchbar-button").click(function () {
    $("#searchbar").toggle("fade", 200)
})


// Hides the alert after 3 seconds
setTimeout(function () {
        $("#msg").animate({'opacity':0}, 3000);
    }, 2000)



// Adds the active class to the active page in nav
// Source - https://stackoverflow.com/questions/26819675/navbar-highlight-for-current-page/26819796
$(function () {
    $('.nav-active').filter(function () {
        return location.href.includes(this.href);
    }).addClass('border-bottom-orange');
});


// Auto increment of the year in footer

const copyrightYearRef = document.querySelector('#copyright-year')

const getFullYear = () => {
    let year = new Date().getFullYear();
    copyrightYearRef.innerHTML = year;
}

getFullYear()
