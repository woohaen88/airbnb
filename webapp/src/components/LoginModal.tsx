import {
  Box,
  Button,
  Input,
  InputGroup,
  InputLeftElement,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  Text,
  VStack,
  useToast,
} from "@chakra-ui/react";
import { FaLock, FaUserNinja } from "react-icons/fa";
import SocialLogin from "./SocialLogin";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { IEmailLoginVariables } from "../api";
import { IEmailLoginError, IEmailLoginSuccess, userEmailLogIn } from "../api";

interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
}

interface IForm {
  email: string;
  password: string;
}

export default function LoginModal({ isOpen, onClose }: LoginModalProps) {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IForm>();
  const toast = useToast();
  const queryClient = useQueryClient();
  const mutation = useMutation<
    IEmailLoginSuccess,
    IEmailLoginError,
    IEmailLoginVariables
  >(userEmailLogIn, {
    onMutate: () => {
      console.log("mutation starting");
    },
    onSuccess: (data) => {
      toast({
        title: "welcome back!",
        status: "success",
      });
      onClose();
      queryClient.refetchQueries(["me"]);
    },
    onError: (error) => {
      console.log("mutation has an error");
    },
  });
  const onSubmit = ({ email, password }: IForm) => {
    mutation.mutate({ email, password });
  };
  return (
    <Modal onClose={onClose} isOpen={isOpen}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Log in</ModalHeader>
        <ModalCloseButton />
        <ModalBody as={"form"} onSubmit={handleSubmit(onSubmit)}>
          <VStack>
            <InputGroup>
              <InputLeftElement
                children={
                  <Box color={"gray.500"}>
                    <FaUserNinja />
                  </Box>
                }
              />

              <Input
                isInvalid={Boolean(errors.email?.message)}
                {...register("email", {
                  required: "please required username",
                })}
                variant={"filled"}
                placeholder="Email"
              />
              <Text fontSize={"sm"} color={"red.500"}>
                {errors.email?.message}
              </Text>
            </InputGroup>

            <InputGroup>
              <InputLeftElement
                children={
                  <Box color={"gray.500"}>
                    <FaLock />
                  </Box>
                }
              />
              <Input
                isInvalid={Boolean(errors.password?.message)}
                {...register("password", {
                  required: "password를 입력해줘 제발~",
                })}
                type="password"
                variant={"filled"}
                placeholder="Password"
              />
              <Text fontSize={"sm"} color={"red.500"}>
                {errors.password?.message}
              </Text>
            </InputGroup>
            {/* {mutation.} */}
          </VStack>
          <Button
            isLoading={mutation.isLoading}
            type="submit"
            mt={4}
            colorScheme="red"
            w={"100%"}
          >
            Log in
          </Button>
          <SocialLogin />
        </ModalBody>
      </ModalContent>
    </Modal>
  );
}
