// Toggle social links container
$("#social-links-button").click(function(){
    $("#social-links").toggle("fade", 200)
})


// Auto increment of the year in footer

const copyrightYearRef = document.querySelector('#copyright-year')

const getFullYear = () => {
    let year = new Date().getFullYear();
    copyrightYearRef.innerHTML = year;
}

getFullYear()