import { Skeleton, Grid, Box, SkeletonText, VStack } from "@chakra-ui/react";

import Room from "../Room";

import { useEffect, useState } from "react";
import RoomSkeleton from "../RoomSkeleton";

// Grid
//   parameters:
//     templateColumns
//     gap
//     columnGap
//     rowGap

//     ex:) templateColumns={"200px 200px 200px ..."}
//          templateColumns={"repeat(5, 1fr)"} // 같은 비율로 5개
//          gap={10}
//          columnGap={4}
//          rowGap={8}
//          templateColumns={"2fr 1fr"} // 첫번째 칼럼이 두번째 칼럼의 2배
interface IPhoto {
  file: string;
  description: string;
  room: number;
  experience: string;
}

interface IRoom {
  id: number;
  name: string;
  country: string;
  city: string;
  price: number;
  rating: number;
  photos: IPhoto[];
}

export default function Home() {
  const [isLoading, setIsLoading] = useState(true);
  const [rooms, setRooms] = useState<IRoom[]>([]);
  const fetchRooms = async () => {
    const response = await fetch("http://localhost:8000/api/v1/room/");
    const json = await response.json();
    setRooms(json);
    setIsLoading(false);
  };
  useEffect(() => {
    fetchRooms();
  }, []);
  return (
    <Grid
      mt={10}
      px={{
        base: 10,
        lg: 40,
      }}
      columnGap={4}
      rowGap={8}
      templateColumns={{
        base: "1fr",
        md: "1fr 1fr",
        lg: "repeat(3, 1fr)",
        xl: "repeat(4, 1fr)",
        "2xl": "repeat(5, 1fr)",
      }}
    >
      {isLoading ? (
        <>
          <RoomSkeleton />
          <RoomSkeleton />
          <RoomSkeleton />
          <RoomSkeleton />
          <RoomSkeleton />
          <RoomSkeleton />
          <RoomSkeleton />
        </>
      ) : null}
      {rooms.map((room) => (
        <Room
          imageUrl={room.photos[0].file}
          name={room.name}
          rating={room.rating}
          city={room.city}
          country={room.country}
          price={room.price}
        />
      ))}
    </Grid>
  );
}
