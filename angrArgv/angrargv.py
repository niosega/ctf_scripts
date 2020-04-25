import angr
import claripy
import time

# This len can be greater than the flag len.
LEN = 28
PGM_NAME = "./exec"
PATTERN = b"WIN"

def win_function(state):
    return PATTERN in state.posix.dumps(1)

def main():
    p = angr.Project(PGM_NAME)

    # arg1 = claripy.BVS("sym_arg", LEN * 8)
    flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(LEN)]
    arg1 = claripy.Concat(*flag_chars)

    st = p.factory.entry_state(args=[PGM_NAME, arg1])

    # for k in flag_chars:
    #     st.solver.add(k != 0)
    #     st.solver.add(k != 10)

    sm = p.factory.simgr(st)
    sm.explore(find=win_function)
    if sm.found:
        s = sm.found[0]
        print(s.solver.eval(arg1, cast_to=bytes))
    else:
        print("NO SOLUTIONS")

if __name__ == "__main__":
    main()