// Args:
// Required:
//     country: str, default: 한국
//     city: str, default: 서울
//     name: str,  v
//     price: int,
//     rooms: int,
//     toilets: int,
//     description: str, default:""
//     address: str, default: ""
//     pet_friendly: bool, default: true
//     kind: choice, [entire_place, private_room, shared_room]

// Optional:
// Relation:
//     [FK] owner: setting.AUTH_USER_MODEL
//     [FK] category: categories.Category
//     [MtoM] amenities: rooms.Amenity

import { FaBed, FaMoneyBill, FaToilet } from "react-icons/fa";
import HostOnlyPage from "./HostOnlyPage";
import ProtectedPage from "./ProtectedPage";
import {
  Box,
  Button,
  Checkbox,
  Container,
  FormControl,
  FormHelperText,
  FormLabel,
  Grid,
  Heading,
  Input,
  InputGroup,
  InputLeftAddon,
  Select,
  Textarea,
  VStack,
  Text,
  useToast,
} from "@chakra-ui/react";
import { useMutation, useQuery } from "@tanstack/react-query";
import {
  IUploadRoomVariables,
  getAmenities,
  getCategories,
  uploadRoom,
} from "../api";
import { IAmenity, ICategory, IRoomDetail } from "../types";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

export default function UploadRoom() {
  const { register, handleSubmit } = useForm<IUploadRoomVariables>();
  const toast = useToast();
  const navigate = useNavigate();
  const mutation = useMutation(uploadRoom, {
    onSuccess: (data: IRoomDetail) => {
      toast({
        status: "success",
        title: "Room created",
        position: "bottom-right",
      });
      navigate(`/room/${data.id}`);
    },
    // onError: () => {},
  });
  const { data: amenities, isLoading: isAmenitiesLoading } = useQuery<
    IAmenity[]
  >(["amenities"], getAmenities);
  const { data: categories, isLoading: isCategoriesLoading } = useQuery<
    ICategory[]
  >(["categories"], getCategories);
  const onSubmit = (data: IUploadRoomVariables) => {
    mutation.mutate(data);
  };

  return (
    <ProtectedPage>
      <HostOnlyPage>
        <Box
          pb={40}
          mt={10}
          px={{
            base: 10,
            lg: 40,
          }}
        >
          <Container>
            <Heading textAlign={"center"}>Upload Room</Heading>
            <VStack
              spacing={10}
              as={"form"}
              mt={5}
              onSubmit={handleSubmit(onSubmit)}
            >
              <FormControl>
                <FormLabel>Name</FormLabel>
                <Input
                  {...register("name", { required: true })}
                  required
                  type="text"
                />
                <FormHelperText>Write the name</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>Country</FormLabel>
                <Input
                  {...register("country", { required: true })}
                  required
                  type="text"
                />
                <FormHelperText>Write the Country</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>City</FormLabel>
                <Input
                  {...register("city", { required: true })}
                  required
                  type="text"
                />
                <FormHelperText>Write the City</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>Address</FormLabel>
                <Input
                  {...register("address", { required: true })}
                  required
                  type="text"
                />
                <FormHelperText>Write the address</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>Price</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaMoneyBill />} />
                  <Input
                    {...register("price", { required: true })}
                    type="number"
                    min={0}
                  />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Rooms</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaBed />} />
                  <Input
                    {...register("rooms", { required: true })}
                    type="number"
                    min={0}
                  />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Toilets</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaToilet />} />
                  <Input
                    {...register("toilets", { required: true })}
                    type="number"
                    min={0}
                  />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Description</FormLabel>
                <Textarea {...register("description", { required: true })} />
              </FormControl>
              <FormControl>
                <Checkbox {...register("pet_friendly", { required: true })}>
                  Pet friendly?
                </Checkbox>
              </FormControl>
              <FormControl>
                <FormLabel>Kind of room</FormLabel>
                <FormHelperText>
                  What kind of room are you renting?
                </FormHelperText>
                <Select
                  {...register("kind", { required: true })}
                  placeholder="Choose ad kind"
                >
                  <option value={"entire_place"}> Entire Place </option>
                  <option value={"private_room"}> Private Room </option>
                  <option value={"shared_room"}> Shared Room </option>
                </Select>
              </FormControl>

              <FormControl>
                <FormLabel>Category</FormLabel>
                <FormHelperText>What kind of Category?</FormHelperText>
                <Select
                  {...register("category", { required: true })}
                  placeholder="Choose a category"
                >
                  {categories?.map((category) => (
                    <option key={category.id} value={category.id}>
                      {category.name}
                    </option>
                  ))}
                </Select>
              </FormControl>
              <FormControl>
                <FormLabel>Amenities</FormLabel>
                <Grid templateColumns={"1fr 1fr"} gap={5}>
                  {amenities?.map((amenity) => (
                    <Box key={amenity.id}>
                      <Checkbox
                        value={amenity.id}
                        {...register("amenities", { required: true })}
                      >
                        {amenity.name}
                      </Checkbox>

                      {amenity.description ? (
                        <FormHelperText>{amenity.description}</FormHelperText>
                      ) : null}
                    </Box>
                  ))}
                </Grid>
              </FormControl>
              {mutation.isError ? (
                <Text color={"red.500"}>Something went wrong</Text>
              ) : null}
              <Button
                isLoading={mutation.isLoading}
                colorScheme="red"
                size={"lg"}
                w={"100%"}
                type="submit"
              >
                Upload Room
              </Button>
            </VStack>
          </Container>
        </Box>
      </HostOnlyPage>
    </ProtectedPage>
  );
}
