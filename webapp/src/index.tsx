import React from "react";
import ReactDOM from "react-dom/client";
import { ChakraProvider, ColorModeScript } from "@chakra-ui/react";
import { RouterProvider } from "react-router-dom";

import router from "./router";
import theme from './theme';
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const client = new QueryClient();

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <QueryClientProvider client={client}>
    <ChakraProvider theme={theme}>
      <ColorModeScript initialColorMode={theme.config.initialColorMode} />
      <RouterProvider router={router} />
    </ChakraProvider>
    </QueryClientProvider>
  </React.StrictMode>
);

// ColorModeScript
// 사용자가 애플리케이션을 이전에 로드했을 때 어떤 색상 테마를 골랐는지 알기 위함
// 사용자가 다크테마를 골랐다면 Chakra가 세팅을 페이지의 로컬 저장소로 저장
// 사용자가 페이지를 새로 고침하거나 해서 다시 로드했을 땐 어떤 테마를 선택했었는지를 다시 불러와야함
// 예를 들어 다크모드라면 사용자가 다크모드를 고르고나서  새로고침 하거나 다시 방문했을 때, 라이트모드를 보여주고 나서 다크모드로 바꾸고 그러는건 안됨
// 그냥 처음부터 다크모드를 보여줘야함
// 이렇게 하려면 Chakra부터 제공되는 `ColorModeScript` 컴포넌트를 추가해야함
// 
// parameter
//  initialColorMode : 사용자 정의 Colormode
//
// 개발자도구 -> application -> localstorage -> chakra-ui-color-mode: light 설정 확인