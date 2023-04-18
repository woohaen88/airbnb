import {extendTheme, type ThemeConfig } from "@chakra-ui/react";

const config:ThemeConfig = {
    initialColorMode:"light",
    useSystemColorMode: false, // 시스템 테마를 따를 것인가?
}


const theme = extendTheme({ config });

export default theme;

