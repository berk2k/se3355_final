
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('registrationForm').addEventListener('submit', function (event) {
        if (!validatePassword()) {
            event.preventDefault(); // Formun submit işlemini durdur
        }
    });
});

document.addEventListener("DOMContentLoaded", function(){
    const citiesDropdown = document.getElementById("city");
  
    fetch('https://run.mocky.io/v3/6d559e1c-92aa-45f1-ad7c-5504fbf9329e')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const cities = data.cities;
  
      cities.forEach(function(city) {
        const option = document.createElement("option");
        option.value = city;
        option.text = city;
        citiesDropdown.appendChild(option);
      });
    })
    .catch(error => console.error('Error fetching data:', error));
  });

function isPasswordValid(password) {
    // En az 8 karakter
    if (password.length < 8) {
        return false;
    }

    // En az 1 rakam
    if (!/\d/.test(password)) {
        return false;
    }

    // En az 1 alfasayısal olmayan karakter
    if (!/\W/.test(password)) {
        return false;
    }

    // Yukarıdaki kriterlere uyuyorsa, şifre geçerli
    return true;
}

function validatePassword() {
    var password = document.getElementById('password').value;
    var isValid = isPasswordValid(password);

    if (!isValid) {
        alert("Invalid password. Please make sure it's at least 8 characters long, contains at least 1 digit, and 1 non-alphanumeric character.");
    }

    return isValid;

}