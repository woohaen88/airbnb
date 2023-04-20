import { Box, Button, Divider, HStack, Text, VStack } from "@chakra-ui/react";
import { FaComment, FaGithub } from "react-icons/fa";

export default function SocialLogin() {
  const kakaoParams = {
    client_id: "c65ba131d4497c8389e078cfbe59469e",
    redirect_uri: "http://localhost:3000/social/kakao",
    response_type: "code",
  };

  const params = new URLSearchParams(kakaoParams).toString();
  return (
    <Box mb={4}>
      <HStack p={8}>
        <Divider />
        <Text
          textTransform={"uppercase"}
          color={"gray.400"}
          fontSize={"xs"}
          as={"b"}
        >
          Or
        </Text>
        <Divider />
      </HStack>
      <VStack>
        <Button
          as="a"
          href="https://github.com/login/oauth/authorize?client_id=e41e6d6c2f43e39f3a7c&scope=read:user,user:email"
          w={"100%"}
          leftIcon={<FaGithub />}
          colorScheme={"telegram"}
        >
          Continue with Github
        </Button>
        <Button
          as={"a"}
          href={`https://kauth.kakao.com/oauth/authorize?${params}`}
          w={"100%"}
          leftIcon={<FaComment />}
          colorScheme={"yellow"}
        >
          Continue with Kakao
        </Button>
      </VStack>
    </Box>
  );
}

// User ========> Github
// Github =======> Website  / 127.0.0.1/confrom-gh?token=AbortController
// abc ============> Django
// Django =================> Github API
