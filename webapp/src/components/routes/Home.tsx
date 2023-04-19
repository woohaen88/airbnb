import { Grid } from "@chakra-ui/react";
import Room from "../Room";
import RoomSkeleton from "../RoomSkeleton";
import { useQuery } from "@tanstack/react-query";
import { getRooms } from "../../api";
import { IRoomList } from "../../types";

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

export default function Home() {
  const { isLoading, data } = useQuery<IRoomList[]>(["rooms"], getRooms);
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
      {data?.map((room) => (
        <Room
          key={room.id}
          id={room.id}
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
