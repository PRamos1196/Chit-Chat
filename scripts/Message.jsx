import React from 'react';

export default function Message(props) {
  return (
    <div className="userNameTextBar">
      <div>{props.message}</div>
    </div>
  );
}