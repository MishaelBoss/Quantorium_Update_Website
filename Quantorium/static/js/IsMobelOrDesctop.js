function getDeviceType() {
  const userAgent = navigator.userAgent.toLowerCase();
  const isMobile = /mobile|iphone|ipad|ipod|android|blackberry|mini|windows\sce|palm/i.test(userAgent);
  const img = document.createElement('img');
  img.src = '/static/icons/profel/desktop.png';

  if (isMobile) {
    document.getElementById('myImage').append(img);
    return "mobile";
  } else {
    document.getElementById('myImage').append(img);
    return "desktop";
  }
}
console.log(getDeviceType());



/*function isMobileDevice() {
  return (
    /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
      navigator.userAgent
    )
  );
}

var image = document.getElementById("myImage");

if (isMobileDevice()) {
  image.src = "/static/icons/profel/phone.png";
} else {
  image.src = "/static/icons/profel/desktop.png";
}*/