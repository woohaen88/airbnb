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
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { getAmenities, getCategories } from "../api";
import { IAmenity, ICategory } from "../types";

export default function UploadRoom() {
  const { data: amenities, isLoading: isAmenitiesLoading } = useQuery<
    IAmenity[]
  >(["amenities"], getAmenities);
  const { data: categories, isLoading: isCategoriesLoading } = useQuery<
    ICategory[]
  >(["categories"], getCategories);
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
            <VStack spacing={10} as={"form"} mt={5}>
              <FormControl>
                <FormLabel>Name</FormLabel>
                <Input required type="text" />
                <FormHelperText>Write the name</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>Country</FormLabel>
                <Input required type="text" />
                <FormHelperText>Write the Country</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>City</FormLabel>
                <Input required type="text" />
                <FormHelperText>Write the City</FormHelperText>
              </FormControl>

              <FormControl>
                <FormLabel>Price</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaMoneyBill />} />
                  <Input type="number" min={0} />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Rooms</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaBed />} />
                  <Input type="number" min={0} />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Toilets</FormLabel>
                <InputGroup>
                  <InputLeftAddon children={<FaToilet />} />
                  <Input type="number" min={0} />
                </InputGroup>
              </FormControl>

              <FormControl>
                <FormLabel>Description</FormLabel>
                <Textarea />
              </FormControl>
              <FormControl>
                <Checkbox>Pet friendly?</Checkbox>
              </FormControl>
              <FormControl>
                <FormLabel>Kind of room</FormLabel>
                <FormHelperText>
                  What kind of room are you renting?
                </FormHelperText>
                <Select placeholder="Choose ad kind">
                  <option value={"entire_place"}> Entire Place </option>
                  <option value={"private_room"}> Private Room </option>
                  <option value={"shared_room"}> Shared Room </option>
                </Select>
                <Checkbox>Pet friendly?</Checkbox>
              </FormControl>

              <FormControl>
                <FormLabel>Category</FormLabel>
                <FormHelperText>What kind of Category?</FormHelperText>
                <Select placeholder="Choose ad kind">
                  {categories?.map((category) => (
                    <option key={category.id} value={category.id}>
                      {category.name}
                    </option>
                  ))}
                </Select>
                <Checkbox>Pet friendly?</Checkbox>
              </FormControl>
              <FormControl>
                <FormLabel>Amenities</FormLabel>
                <Grid templateColumns={"1fr 1fr"} gap={5}>
                  {amenities?.map((amenity) => (
                    <Box key={amenity.id}>
                      <Checkbox>{amenity.name}</Checkbox>

                      {amenity.description ? (
                        <FormHelperText>{amenity.description}</FormHelperText>
                      ) : null}
                    </Box>
                  ))}
                </Grid>
              </FormControl>
              <Button colorScheme="red" size={"lg"} w={"100%"}>
                Upload Room
              </Button>
            </VStack>
          </Container>
        </Box>
      </HostOnlyPage>
    </ProtectedPage>
  );
}
