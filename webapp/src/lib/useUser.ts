import { useQuery } from "@tanstack/react-query";
import { getMe } from "../api";
import { User } from "../types";

export default function useUser() {
  const { isLoading, data, isError } = useQuery<User>([`me`], getMe, {
    retry: false,
  });

  return {
    userLoading: isLoading,
    user: data,
    isLoggedIn: !isError,
  };
}
