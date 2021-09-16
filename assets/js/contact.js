let loader = document.getElementById('loader');
let FD = new FormData();
let subFrm = document.getElementById('f-submit');

subFrm.addEventListener('click', () => {

    if (subFrm.innerText === 'Thank You') {
        displayMsg("Our team is on it's way to heal your growth\nCheck your mail for further details", 'f-success')
    } else {


        loader.style.display = 'flex'

        // getting  details
        let clNameD = document.getElementById('cl-name');
        let clMailD = document.getElementById('cl-mail');
        let clPurD = document.getElementById('cl-purpose');
        let clQotD = document.getElementById('cl-quote');
        let clOrgNameD = document.getElementById('cl-org-na');
        let clOrgWebD = document.getElementById('cl-org-web');

        let clName = clNameD.value.trim();
        let clMail = clMailD.value.trim();
        let clPur = clPurD.value;
        let clQot = clQotD.value.trim();
        let clOrgName = clOrgNameD.value.trim();
        let clOrgWeb = clOrgWebD.value.trim();


        if (checkName() && checkEmail() && checkPurpose() && checkQuote()) {
            subFrm.innerText = 'SENDING'
            formData();
            const url = window.location.href;
            const xhr = new XMLHttpRequest();
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

            xhr.open("POST", url + `service-request/`, true)
            xhr.setRequestHeader("X-CSRFToken", csrfToken)
            xhr.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {
                    resetForm();
                    displayMsg('Thank you 💙 for your request we are working for your growth\nCheck your mail for further details', 'f-success')
                    subFrm.innerText = 'Thank You'
                    loader.style.display = 'none'
                } else {
                    displayMsg('🔴 Oops there was an unexpected error 🔴\nplease resubmit', 'f-error')
                    subFrm.innerText = 'Try Again'
                    loader.style.display = 'none'
                }
            };
            xhr.send(FD);
        }


        function resetForm() {
            clNameD.value = "";
            clMailD.value = "";
            clOrgNameD.value = "";
            clOrgWebD.value = "";
            clPurD.value = "default";
            clQotD.value = "";

        }

        function checkName() {
            if (clName === '') {
                displayMsg('Can we know your name please 🤔', 'f-error');
            } else {
                return true;
            }
        }

        function checkEmail() {
            let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$/;
            if (clMail === '') {
                displayMsg('Enter your E-mail for us to reach out to you', 'f-error')
            } else if (emailPattern.test(clMail) === false) {
                displayMsg('Oops was there a typo 😳\nE-mail pattern should be xxxx@domain.com', 'f-error')
            } else {
                return true;
            }
        }

        function checkPurpose() {
            if (clPur === 'default') {
                displayMsg('* Select the Purpose of enquiry for us to know you better', 'f-error');
            } else {
                return true;
            }
        }

        function checkQuote() {
            if (clQot === '') {
                displayMsg("* Put in your quote\nThis let's us server your better 💙", 'f-error');
            } else if (clQot === '0') {
                displayMsg('We are sure we worth more than that 😫', 'f-error');
            } else {
                return true;
            }
        }

        function formData() {
            FD.append("client-name", clName);
            FD.append("client-mail", clMail);
            FD.append("org-name", clOrgName);
            FD.append("org-web", clOrgWeb);
            FD.append("client-request", clPur);
            FD.append("client-quote", clQot);
            let nowDate = new Date().toString()
            FD.append("request-time", nowDate);
        }
    }
});

function displayMsg(msg, action) {
    let errorMsg = document.getElementById('errorD');
    loader.style.display = 'none'
    errorMsg.className = action;
    errorMsg.innerText = msg;
}