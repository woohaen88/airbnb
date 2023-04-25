import {
  Box,
  Button,
  Container,
  FormControl,
  Heading,
  Input,
  VStack,
} from "@chakra-ui/react";
import ProtectedPage from "../ProtectedPage";
import { useForm } from "react-hook-form";
import { useParams } from "react-router-dom";

export default function UploadPhotos() {
  const { register, watch } = useForm();
  const { roomId } = useParams();
  return (
    <ProtectedPage>
      <Box
        pb={40}
        mt={10}
        px={{
          base: 10,
          lg: 40,
        }}
      >
        <Container>
          <Heading textAlign={"center"}>Upload a photo</Heading>
          <VStack as={"form"} spacing={5} mt={10}>
            <FormControl>
              <Input {...register("file")} type={"file"} accept="image/*" />
            </FormControl>
            <Button type="submit" w={"full"} colorScheme="red">
              Upload Photo
            </Button>
          </VStack>
        </Container>
      </Box>
    </ProtectedPage>
  );
}
