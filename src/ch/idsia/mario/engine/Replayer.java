package ch.idsia.mario.engine;

import java.io.*;


public class Replayer
{
    private ByteArrayInputStream bais;
    private DataInputStream dis;

    private byte tick = 0;
    private int tickCount = -99999999;

    public Replayer(byte[] bytes)
    {
        bais = new ByteArrayInputStream(bytes);
        dis = new DataInputStream(bais);
    }

    public long nextLong()
    {
        try
        {
            return dis.readLong();
        }
        catch (IOException e)
        {
            e.printStackTrace();
            return 0;
        }
    }

    public byte nextTick()
    {
        if (tickCount == -99999999)
        {
            try
            {
                tickCount = dis.readInt();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }

        if (tickCount == 0)
        {
            try
            {
                tick = (byte) dis.read();
                tickCount = dis.readInt();
            }
            catch (IOException e)
            {
            }
        }
        
        if (tickCount>0)
        {
            tickCount--;
        }

        return tick;
    }
}