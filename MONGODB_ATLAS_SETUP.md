# MongoDB Atlas Configuration Guide

## Overview
This guide will help you configure your Finance AI Assistant application to use MongoDB Atlas instead of a local MongoDB instance.

## Prerequisites
1. A MongoDB Atlas account (sign up at https://www.mongodb.com/atlas)
2. A MongoDB Atlas cluster created
3. Network access configured (allow your IP or 0.0.0.0/0 for all IPs)

## Step 1: Get Your MongoDB Atlas Connection String

1. **Log in to MongoDB Atlas**: Go to https://cloud.mongodb.com/
2. **Select your cluster**: Click on your cluster name
3. **Click "Connect"**: In the cluster overview
4. **Choose connection method**: Select "Connect your application"
5. **Copy the connection string**: It will look like:
   ```
   mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
   ```

## Step 2: Update Environment Variables

1. **Open the `.env` file** in the `backend/` directory
2. **Replace the MONGODB_URI** with your Atlas connection string:
   ```env
   MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/?retryWrites=true&w=majority
   ```
3. **Update the DATABASE_NAME** if needed (default: `finance_db`):
   ```env
   DATABASE_NAME=your_desired_database_name
   ```

## Step 3: Configure Network Access

### Option A: Allow Specific IP (Recommended for Production)
1. In MongoDB Atlas dashboard, go to **Network Access**
2. Click **Add IP Address**
3. Add your current IP address or your server's IP

### Option B: Allow All IPs (For Development/Testing)
1. In MongoDB Atlas dashboard, go to **Network Access**
2. Click **Add IP Address**
3. Enter `0.0.0.0/0` and confirm

## Step 4: Create Database User (if needed)

1. In MongoDB Atlas dashboard, go to **Database Access**
2. Click **Add New Database User**
3. Choose **Password** authentication
4. Set username and password
5. Grant **Read and write** permissions to your database

## Step 5: Test the Connection

1. **Start the application**:
   ```bash
   cd backend
   python run.py serve
   ```

2. **Check the console output**: You should see successful connection logs

3. **Test API endpoint**: Visit `http://localhost:8000/` - should return:
   ```json
   {
     "status": "ok",
     "service": "Finance AI Assistant",
     "version": "1.0.0"
   }
   ```

## Troubleshooting

### Common Issues:

1. **Authentication Failed**
   - Check username/password in connection string
   - Ensure database user has correct permissions

2. **Connection Timeout**
   - Check network access settings in Atlas
   - Verify your IP is whitelisted

3. **SSL/TLS Issues**
   - Atlas requires SSL connections
   - The connection string already includes SSL parameters

4. **Connection String Format**
   - Ensure you're using `mongodb+srv://` for Atlas (not `mongodb://`)
   - Include all required parameters: `?retryWrites=true&w=majority`

### Security Best Practices:

1. **Use strong passwords** for database users
2. **Restrict IP access** in production (don't use 0.0.0.0/0)
3. **Rotate credentials** regularly
4. **Monitor Atlas logs** for suspicious activity
5. **Use different databases** for different environments (dev/staging/prod)

## Configuration Files Modified:
- `backend/.env` - Updated with Atlas connection string format

## Next Steps:
After successful configuration, your application will:
- Connect to MongoDB Atlas on startup
- Store all data in the cloud
- Have automatic failover and backup (Atlas features)
- Scale horizontally if needed

## Support:
- MongoDB Atlas Documentation: https://docs.atlas.mongodb.com/
- Connection Issues: Check Atlas cluster logs and connection metrics
