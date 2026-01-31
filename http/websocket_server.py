import asyncio
import websockets

async def handler(ws):
    async for msg in ws:
        await ws.send("Echo: " + msg)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[WebSocket] Server running on port 8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
