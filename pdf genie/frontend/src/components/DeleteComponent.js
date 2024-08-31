
import React from 'react';

function DeleteComponent() {

  const handleDelete = () => {
    fetch('http://localhost:5000/delete', {
      method: 'DELETE',
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <button onClick={handleDelete}>Delete Uploaded Files</button>
    </div>
  );
}

export default DeleteComponent;
