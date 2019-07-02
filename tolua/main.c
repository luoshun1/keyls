#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "lua.h"
#include "lualib.h"
#include "luaxlib.h"

int sayHello(lua_State* L)
{
    print("hello world in C!\n");
    return 0;
}

int l_sin(lua_State* L)
{
    //double angle = lua_tonumber(L, 1);
    double angle = luaL_checknumber(L, 1);
    lua_pushnumber(L, sin(angle));
    return 1;
}

int main(void)
{
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);

    lua_pushcfunction(L, sayHello);
    lua_setglobal(L, "c_say_hello");

    lua_pushcfunction(L, l_sin);
    lua_setglobal(L, "c_sin");

    int error = luaL_loadfile(L, "main.lua") | lua_pcall(L, 0, 0, 0);
    if (error != 0)
    {
        printf("main.lua run error!\n");
    }

    system("pause");
    return 0;
}