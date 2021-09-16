// cookie display controller
let cookieDiv = document.getElementById('cookie-content');
let cAcceptBtn = document.getElementById('c-accept-btn');

if (!sessionStorage.getItem("htm-cookie-status")) {
    cookieDiv.style.display = 'block';
}

cAcceptBtn.addEventListener('click', () => {
    cookieDiv.style.display = 'none';
    sessionStorage.setItem("htm-cookie-status", "on");
});

// email subscribe handler
let subBtn = document.getElementById('cu-msb');

subBtn.addEventListener('click', () => {
    displayMsg("Submitting . . .", 'f-success');

    //getting details
    let subMail = document.getElementById('sub-mail');

    if (checkEmail()) {
        let FD = new FormData();
        FD.append("subscriber-mail", subMail.value.trim());
        const url = window.location.href;
        const xhr = new XMLHttpRequest();
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

        xhr.open("POST", url + `mail-subscription/`, true)
        xhr.setRequestHeader("X-CSRFToken", csrfToken)
        xhr.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                subMail.value = '';
                let response = this.responseText
                response = JSON.parse(response)
                if (response['status'] === '1')
                    displayMsg(response['message'], 'f-success')
                else if (response['status'] === '0')
                    displayMsg(response['message'], 'f-success')
            } else {
                displayMsg('🔴 Oops there was an unexpected error 🔴\nplease resubmit', 'f-error')
            }
        };
        xhr.send(FD);
    }

    function checkEmail() {
        let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$/;
        if (subMail.value.trim() === '') {
            displayMsg('Your subscription is all most done, but we need your mail id', 'f-error')
        } else if (emailPattern.test(subMail.value.trim()) === false) {
            displayMsg('Oops was there a typo 😳\nE-mail pattern should be xxxx@domain.com', 'f-error')
        } else {
            return true;
        }
    }

});

function displayMsg(msg, action) {
    let errorMsg = document.getElementById('errorD');
    errorMsg.className = action;
    errorMsg.innerText = msg;
}
