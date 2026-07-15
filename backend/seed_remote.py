import asyncio
import asyncpg
from passlib.context import CryptContext
import uuid
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def main():
    db_url = "postgresql://neondb_owner:npg_Jn9tc2NSRpYA@ep-summer-sound-atfdgtuj.c-9.us-east-1.aws.neon.tech/neondb?ssl=require"
    print("Connecting to DB to insert users...")
    conn = await asyncpg.connect(db_url)
    
    hashed_password = pwd_context.hash("admin123")
    user_id = str(uuid.uuid4())
    await conn.execute(
        '''
        INSERT INTO users (id, email, hashed_password, first_name, last_name, primary_role, is_active, is_verified, created_at, updated_at, is_deleted)
        VALUES ($1, 'rajesh.kumar@hrcopilot.io', $2, 'Rajesh', 'Kumar', 'SUPER_ADMIN', true, true, $3, $3, false)
        ON CONFLICT (email) DO NOTHING
        ''',
        user_id, hashed_password, datetime.datetime.now(datetime.timezone.utc)
    )
    print("Admin inserted.")
    
    hashed_password_demo = pwd_context.hash("demo123")
    user_id2 = str(uuid.uuid4())
    await conn.execute(
        '''
        INSERT INTO users (id, email, hashed_password, first_name, last_name, primary_role, is_active, is_verified, created_at, updated_at, is_deleted)
        VALUES ($1, 'arjun.sharma@hrcopilot.io', $2, 'Arjun', 'Sharma', 'EMPLOYEE', true, true, $3, $3, false)
        ON CONFLICT (email) DO NOTHING
        ''',
        user_id2, hashed_password_demo, datetime.datetime.now(datetime.timezone.utc)
    )
    print("Demo user inserted.")
    
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
