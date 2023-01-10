def simplifyPath(path: str) -> str:
    stack = []
    
    for part in path.split("/"):

        if not part or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


print(simplifyPath("/home//foo/"))