let hDnvxDIc = document.getElementById('hDnvxD-ic');
let hDNvD = document.getElementById('hD-nvD');
let hDNvDCtr = 0;
hDnvxDIc.addEventListener('click', () => {
    if (hDNvDCtr === 0) {
        hDNvD.style.display = 'grid';
        hDNvDCtr = 1;
    } else if (hDNvDCtr === 1) {
        hDNvD.style.display = 'none';
        hDNvDCtr = 0;
    }
});
