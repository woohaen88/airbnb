import {
  Box,
  Button,
  HStack,
  IconButton,
  useDisclosure,
  useColorMode,
  useColorModeValue,
  Stack,
  Avatar,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  useToast,
} from "@chakra-ui/react";
import { FaAirbnb, FaMoon, FaSun } from "react-icons/fa";
import LoginModal from "./LoginModal";
import SignUpModal from "./SignUpModal";
import useUser from "../lib/useUser";
import { logOut } from "../api";
import { useQueryClient } from "@tanstack/react-query";

export default function Header() {
  const { userLoading, isLoggedIn, user } = useUser();
  const {
    isOpen: isLoginOpen,
    onClose: onLoginClose,
    onOpen: onLoginOpen,
  } = useDisclosure();
  const {
    isOpen: isSignUpOpen,
    onClose: onSignUpClose,
    onOpen: onSignUpOpen,
  } = useDisclosure();

  // ColorModeScript을 boolean으로 사용하려면 useColorMode라는 hook을 사용
  const { toggleColorMode } = useColorMode(); // value, function
  const logoColor = useColorModeValue("red.500", "red.200"); // light, dark
  const Icon = useColorModeValue(FaMoon, FaSun); // 컴포넌트는 첫글자가 대문자
  const toast = useToast();
  const queryClient = useQueryClient();
  const onLogOut = async () => {
    await logOut();
    queryClient.refetchQueries(["me"]);
    const toastId = toast({
      title: "Login out ...",
      description: "see you",
      status: "loading",
      position: "bottom-right",
    });

    setTimeout(() => {
      toast.update(toastId, {
        status: "success",
        title: "Done!",
        description: "See you later",
      });
    }, 1000);
  };

  return (
    <Stack
      justifyContent={"space-between"}
      py={5}
      px={40}
      direction={{
        sm: "column",
        md: "row",
      }}
      spacing={{
        sm: 4,
        md: 0,
      }}
      alignItems="center"
      borderBottomWidth={1}
    >
      <Box color={logoColor}>
        <FaAirbnb size={"48"} />
      </Box>
      <HStack spacing={2}>
        <IconButton
          onClick={toggleColorMode}
          variant={"ghost"}
          aria-label="Toggle dark mode"
          icon={<Icon />}
        ></IconButton>

        {!userLoading ? (
          !isLoggedIn ? (
            <>
              <Button onClick={onLoginOpen}>Log in</Button>
              <Button onClick={onSignUpOpen} colorScheme={"red"}>
                Sign up
              </Button>
            </>
          ) : (
            <Menu>
              <MenuButton>
                <Avatar name={user?.username} size={"md"} src={user?.avatar} />
              </MenuButton>
              <MenuList>
                <MenuItem onClick={onLogOut}>Log out</MenuItem>
              </MenuList>
            </Menu>
          )
        ) : null}
      </HStack>

      <LoginModal isOpen={isLoginOpen} onClose={onLoginClose} />
      <SignUpModal isOpen={isSignUpOpen} onClose={onSignUpClose} />
    </Stack>
  );
}
