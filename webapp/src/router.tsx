import { createBrowserRouter } from "react-router-dom";
import Root from "./components/Root";
import Home from "./components/routes/Home";
import NotFound from "./components/routes/NotFound";
import RoomDetail from "./components/routes/RoomDetail";
import GithubConfirm from "./components/routes/GithubConfirm";
import KakaoConfirm from "./components/routes/KakaoConfirm";
import UploadRoom from "./components/UploadRoom";
import UploadPhotos from "./components/routes/UploadPhotos";
const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <NotFound />,
    children: [
      {
        path: "",
        element: <Home />,
      },
      {
        path: "room/upload",
        element: <UploadRoom />,
      },
      {
        path: "room/:roomId",
        element: <RoomDetail />,
      },
      {
        path: "room/:roomId/photos",
        element: <UploadPhotos />,
      },
      {
        path: "social",
        children: [
          {
            path: "github",
            element: <GithubConfirm />,
          },
          {
            path: "kakao",
            element: <KakaoConfirm />,
          },
        ],
      },
    ],
  },
]);

export default router;
