const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let submit_btn = document.getElementById('submit_btn');
let msgDiv = document.getElementById('status-msg');

let FD = new FormData();
FD.append('s_id', sId);
FD.append('current_state', currentPrefState);
FD.append('action_hash', actionHash);
submit_btn.addEventListener('click', () => {
    msgDiv.innerText = 'Requesting Update';
    msgDiv.style.display = 'flex';
    msgDiv.className = 'status-msg st-m-success';

    pref_state_check();

    const url = 'http://127.0.0.1:8000/subscriber-action/';
    const xhr = new XMLHttpRequest();
    xhr.open("POST", url + `action-status/preference-update/`, true);
    xhr.setRequestHeader("X-CSRFToken", csrfToken)
    xhr.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            msgDiv.className = 'status-msg st-m-success';
            msgDiv.innerText = 'Request sent';
            let response = this.responseText
            response = JSON.parse(response);
            sleep(1000).then(() => {
                msgDiv.innerText = 'Redirecting your request';
                sleep(1000).then(() => {
                    window.location.replace(url + response['redirect_url']);
                });
            });
        } else {
            msgDiv.className = 'status-msg st-m-error';
            msgDiv.innerText = 'Oops there was a glitch 😳 !! Please try again';
        }
    };
    xhr.send(FD)
})

function pref_state_check() {
    let info_checkbox = document.getElementById('info_box'),
        promo_checkbox = document.getElementById('promo_box'),
        info_status = false,
        promo_status = false;
    if (info_checkbox.checked === true)
        info_status = true
    if (promo_checkbox.checked === true)
        promo_status = true

    FD.append('info_state', info_status.toString());
    FD.append('promo_state', promo_status.toString());
}

//sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}