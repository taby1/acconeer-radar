Import("env")

# Operate with the project environment (files located in the `src` folder)
Import("projenv")


# projenv.Append(CPPDEFINES=[
#   "PROJECT_EXTRA_MACRO_1_NAME",
#   ("ROJECT_EXTRA_MACRO_2_NAME", "ROJECT_EXTRA_MACRO_2_VALUE")
# ])
# projenv.Append(CCFLAGS=[
#   "PROJECT_EXTRA_MACRO_1_NAME",
#   ("ROJECT_EXTRA_MACRO_2_NAME", "ROJECT_EXTRA_MACRO_2_VALUE")
# ])

projenv.Append(LIBPATH=[projenv["PROJECT_LIBDEPS_DIR"]+"/"+projenv["PIOENV"] + "/acconeer-radar/include"])
# projenv.Append(LIBPATH=["ayooooo"])
# print(projenv.Dump())

# print("asldkfasldkfjalskdjfasdf")
# print("wtf")
# # add (prepend) to the beginning of list
# projenv.Prepend(CPPPATH=["some/path"])
# # remove specified flags
# projenv.ProcessUnFlags("-fno-rtti")

# Pass flags to the Global environemnt (project `src` files, frameworks)
# global_env = DefaultEnvironment()
# global_env.Append(CPPDEFINES=[("TEST_GLOBAL", 1)])
# global_env.Append(CCFLAGS=[("TEST_GLOBAL", 1)])

