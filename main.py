import sys
import Flow from flow

if __name__ == "__main__":
    try:
        concurrency = int(sys.argv[2])
    except ValueError:
        text = f"Usage: python3 {sys.argv[0]} <numOfParallelScripts"
        print(text)

    wf = Workflow(concurrency)
    wf.load()
    wf.start()

