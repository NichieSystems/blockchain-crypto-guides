const startRamp = () => {
    new rampInstantSdk.RampInstantSDK({
        hostAppName: 'Scurdex',
        hostLogoUrl: 'https://s3.us-east-2.amazonaws.com/files.scurdex.com/scurdex_logo.svg',
        userAddress: 'user blockchain address',
        defaultAsset: 'BTC',
        swapAmount: '150000000000000000000',
        finalUrl: 'https://www.scurdex.com',
        fiatCurrency: 'USD',
        fiatValue: 150,
        variant: 'auto',
        // url: 'https://ri-widget-staging.firebaseapp.com',
        hostApiKey: 'cmshb5cfbdg3d88ruu8o45rmgkf8g5265ts9j2og',
    })
    .on('*', (event) => console.log(event))
    .show();
}
document.querySelector('#buy-with-ramp-button').addEventListener('click', startRamp); 
