const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let submit_btn = document.getElementById('submit-btn');
let msgDiv = document.getElementById('status-msg');

let FD = new FormData();
FD.append('s_id', sId);
FD.append('action_hash', actionHash);

submit_btn.addEventListener('click', () => {
    msgDiv.innerText = 'Requesting Unsubscription';
    msgDiv.style.display = 'flex';
    msgDiv.className = 'status-msg st-m-success';

    uns_state_check();

    const url = 'http://127.0.0.1:8000/subscriber-action/';
    const xhr = new XMLHttpRequest();
    xhr.open("POST", url + `action-status/unsubscribe/`, true);
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            msgDiv.className = 'status-msg st-m-success';
            msgDiv.innerText = 'Request sent';
            let response = this.responseText;
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
    }
    xhr.send(FD);

});

function uns_state_check() {
    let unSb1 = document.getElementById('un-sb1'),
        unSb2 = document.getElementById('un-sb2'),
        unSb3 = document.getElementById('un-sb3'),
        unSbC = document.getElementById('un-sub-txt'),
        unSb1State = '0',
        unSb2State = '0',
        unSb3State = '0';
    if (unSb1.checked === true)
        unSb1State = '1';
    if (unSb2.checked === true)
        unSb2State = '1';
    if (unSb3.checked === true)
        unSb3State = '1';
    FD.append('un_sub_state', (unSb1State + unSb2State + unSb3State).toString());
    FD.append('un_sub_cmt', unSbC.value.toString());
}

//sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}