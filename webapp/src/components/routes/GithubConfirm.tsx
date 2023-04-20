import {
  Button,
  Heading,
  Spinner,
  Text,
  VStack,
  useToast,
} from "@chakra-ui/react";
import { useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { githubLogIn } from "../../api";
import { useQueryClient } from "@tanstack/react-query";

export default function GithubConfirm() {
  // 화면이 처음 나타났을 때 url에서 http://localhost:3000/social/github?code=xxxxxxxxxxxxxxxxx
  // 코드 값을 가져오기 위해 useLocation Hook을 사용

  const toast = useToast();
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const confirmLogin = async () => {
    const params = new URLSearchParams(search);
    const code = params.get("code");
    if (code) {
      const status = await githubLogIn(code);
      if (status === 200) {
        toast({
          status: "success",
          title: "Welcome!",
          position: "bottom-right",
          description: "Happy to have you back!",
        });
        queryClient.refetchQueries(["me"]);
        navigate("/");
      }
    }
  };
  const { search } = useLocation();
  useEffect(() => {
    confirmLogin();
  }, []);
  return (
    <VStack justifyContent={"center"} mt={40}>
      <Heading>Processing log in...</Heading>
      <Text> Don't go anywhere </Text>
      <Spinner size={"lg"} />
    </VStack>
  );
}
