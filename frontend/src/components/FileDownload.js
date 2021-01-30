import React, { useEffect, useState } from "react";
const db = require("mime-db");

const FileDownload = () => {
  const [downloadLink, setDownloadLink] = useState("");
  const [downloadFile, setDownloadFile] = useState(null);
  const [downloadName, setDownloadName] = useState("");

  const getFile = async () => {
    await fetch("download_request", { method: "POST" }).then((response) => {
      if (response.ok) {
        response.blob().then((data) => {
          setDownloadName("file" + db[data.type].extensions[0]);
          setDownloadFile(data);
          setDownloadLink(window.URL.createObjectURL(data));
        });
      } else alert("file not found");
    });
  };

  const handleClick = async (event) => {
    event.preventDefault();
    if (!downloadFile) await getFile();
  };

  return (
    <div>
      <button onClick={handleClick}>Prepare file</button>
      <a download={downloadLink ? downloadName : null} href={downloadLink}>
        {downloadLink ? "Click here to download" : ""}
      </a>
    </div>
  );
};

export default FileDownload;
