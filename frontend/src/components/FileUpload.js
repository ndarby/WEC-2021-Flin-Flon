import React, { useState } from "react";

const FileUpload = () => {
  const [fileInput, setFileInput] = useState(null);

  // const handleFileChange = (event) => {
  //   event.preventDefault();
  //   setSelectedFile(event.target.files[0]);
  // };

  const handleFileUpload = async (event) => {
    event.preventDefault();

    const data = new FormData();
    data.append("file", fileInput.files[0]);

    await fetch("upload_request", { method: "POST", body: data })
      .then((response) => {
        response
          .json()
          .then((body) => {
            alert(body.message);
          })
          .catch((error) => alert(`error uploading file: ${error}`));
      })
      .catch((error) => alert(`error uploading file: ${error}`));
  };

  return (
    <form>
      <input type="file" ref={(ref) => setFileInput(ref)} />
      <button onClick={handleFileUpload}>upload</button>
    </form>
  );
};

export default FileUpload;
