import { QueryFunctionContext } from "@tanstack/react-query";
import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
});

export const getRooms = () =>
  instance.get("room/").then((response) => response.data);

export const getRoom = ({ queryKey }: QueryFunctionContext) => {
  const [_, roomId] = queryKey;
  return instance.get(`room/${roomId}`).then((response) => response.data);
};
