import { QueryFunctionContext } from "@tanstack/react-query";
import axios from "axios";
import Cookie from "js-cookie";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
  withCredentials: true,
});

export const getRooms = () =>
  instance.get("room/").then((response) => response.data);

export const getRoom = ({ queryKey }: QueryFunctionContext) => {
  const [_, roomId] = queryKey;
  return instance.get(`room/${roomId}`).then((response) => response.data);
};

export const getRoomReviews = ({ queryKey }: QueryFunctionContext) => {
  const [_, roomId] = queryKey;
  return instance
    .get(`room/${roomId}/reviews`)
    .then((response) => response.data);
};

export const getMe = () => {
  return instance.get(`user/me/`).then((response) => response.data);
};

export const logOut = () => {
  return instance
    .post(`user/logout/`, null, {
      headers: {
        "X-CSRFToken": Cookie.get("csrftoken") || "",
      },
    })
    .then((response) => response.data);
};

export const githubLogIn = (code: string) => {
  return instance
    .post(
      `user/github/`,
      { code },
      {
        headers: {
          "X-CSRFToken": Cookie.get("csrftoken") || "",
        },
      }
    )
    .then((response) => response.status);
};

export const kakaoLogIn = (code: string) => {
  return instance
    .post(
      `user/kakao/`,
      { code },
      {
        headers: {
          "X-CSRFToken": Cookie.get("csrftoken") || "",
        },
      }
    )
    .then((response) => response.status);
};


export interface IEmailLoginVariables {
  email: string;
  password: string;
}

export interface IEmailLoginSuccess {
  message: string
}

export interface IEmailLoginError {
  non_field_errors: string[]
}

export const userEmailLogIn = ({email, password}:IEmailLoginVariables) => {
  return instance.post(
    "user/user-login/",
    {email, password},
    {
      headers: {
        "X-CSRFToken": Cookie.get("csrftoken") || "",
      },
    }
  ).then((response) => response.data)
}