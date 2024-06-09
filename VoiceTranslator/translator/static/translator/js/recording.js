const recordButton = document.getElementById("record_btn");
const translateForm = document.getElementById("translate_form");
const recordField = document.getElementById("record_field");
var voice_recorded = false;

navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
	const mediaRecorder = new MediaRecorder(stream);

	const audioChunks = [];
	mediaRecorder.addEventListener("dataavailable", (event) => {
		audioChunks.push(event.data);
	});

	mediaRecorder.addEventListener("stop", () => {
		const audioBlob = new Blob(audioChunks);

		var reader = new FileReader();
		reader.readAsDataURL(audioBlob);
		reader.onloadend = function () {
			var base64String = reader.result;
			recordField.setAttribute("value", base64String);
			translateForm.submit();
		};
	});

	recordButton.addEventListener("click", () => {
		if (voice_recorded == false) {
			voice_recorded = true;
			mediaRecorder.start();
			recordButton.classList.remove("rec-button");
			recordButton.classList.add("rec-stop-button");
		} else {
			mediaRecorder.stop();
			recordButton.classList.add("rec-button");
			recordButton.classList.remove("rec-stop-button");
		}
	});
});
