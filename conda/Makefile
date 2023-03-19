# set the compiler
CXX = g++

# set compiler flags
CXXFLAGS = -std=c++11 -Wall -Wextra -Wpedantic

# set source files
SRCS = hello.cpp my_math.cpp

# set object files
OBJS = $(SRCS:.cpp=.o)

# set executable name
EXE = hello

# build executable
$(EXE): $(OBJS)
	$(CXX) $(OBJS) -o $(EXE)

# build object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# clean up
clean:
	rm -f $(OBJS) $(EXE)

