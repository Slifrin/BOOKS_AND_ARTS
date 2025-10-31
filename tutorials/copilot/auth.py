#!/usr/bin/env python3
"""
OAuth Authentication Module
Provides OAuth 2.0 authentication functionality using only Python standard library.
Supports Authorization Code flow with PKCE (Proof Key for Code Exchange).
"""

import urllib.parse
import urllib.request
import urllib.error
import json
import secrets
import hashlib
import base64
import webbrowser
import http.server
import threading
import time
from typing import Dict, Optional, Tuple, Any

class OAuthConfig:
    """OAuth configuration container."""
    
    def __init__(self, 
                 client_id: str,
                 client_secret: str = "",
                 authorization_url: str = "",
                 token_url: str = "",
                 redirect_uri: str = "http://localhost:8080/callback",
                 scope: str = ""):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_url = authorization_url
        self.token_url = token_url
        self.redirect_uri = redirect_uri
        self.scope = scope

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    """HTTP handler for OAuth callback."""
    
    def __init__(self, *args, oauth_client=None, **kwargs):
        self.oauth_client = oauth_client
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET request to callback endpoint."""
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        if 'code' in query_params:
            # Success - authorization code received
            auth_code = query_params['code'][0]
            state = query_params.get('state', [None])[0]
            
            # Store the authorization code
            if self.oauth_client:
                self.oauth_client.auth_code = auth_code
                self.oauth_client.callback_state = state
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <head><title>Authentication Successful</title></head>
                <body>
                    <h1>Authentication Successful!</h1>
                    <p>You can close this window and return to the application.</p>
                    <script>window.close();</script>
                </body>
                </html>
            """)
        
        elif 'error' in query_params:
            # Error case
            error = query_params['error'][0]
            error_description = query_params.get('error_description', [''])[0]
            
            if self.oauth_client:
                self.oauth_client.auth_error = f"{error}: {error_description}"
            
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"""
                <html>
                <head><title>Authentication Error</title></head>
                <body>
                    <h1>Authentication Error</h1>
                    <p>Error: {error}</p>
                    <p>Description: {error_description}</p>
                </body>
                </html>
            """.encode())
        
        else:
            # Unknown request
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """Suppress default logging."""
        pass

class OAuthClient:
    """OAuth 2.0 client with PKCE support."""
    
    def __init__(self, config: OAuthConfig):
        self.config = config
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.token_expires_at: Optional[float] = None
        self.auth_code: Optional[str] = None
        self.callback_state: Optional[str] = None
        self.auth_error: Optional[str] = None
        
        # PKCE parameters
        self.code_verifier: Optional[str] = None
        self.code_challenge: Optional[str] = None
        self.state: Optional[str] = None
    
    def _generate_pkce_parameters(self) -> Tuple[str, str]:
        """Generate PKCE code verifier and challenge."""
        # Code verifier: random string 43-128 characters
        code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8').rstrip('=')
        
        # Code challenge: SHA256 hash of verifier, base64url encoded
        challenge_bytes = hashlib.sha256(code_verifier.encode('utf-8')).digest()
        code_challenge = base64.urlsafe_b64encode(challenge_bytes).decode('utf-8').rstrip('=')
        
        return code_verifier, code_challenge
    
    def _generate_state(self) -> str:
        """Generate random state parameter for CSRF protection."""
        return secrets.token_urlsafe(32)
    
    def get_authorization_url(self) -> str:
        """Generate authorization URL for OAuth flow."""
        # Generate PKCE parameters
        self.code_verifier, self.code_challenge = self._generate_pkce_parameters()
        self.state = self._generate_state()
        
        params = {
            'response_type': 'code',
            'client_id': self.config.client_id,
            'redirect_uri': self.config.redirect_uri,
            'scope': self.config.scope,
            'state': self.state,
            'code_challenge': self.code_challenge,
            'code_challenge_method': 'S256'
        }
        
        # Remove empty parameters
        params = {k: v for k, v in params.items() if v}
        
        query_string = urllib.parse.urlencode(params)
        return f"{self.config.authorization_url}?{query_string}"
    
    def start_callback_server(self, port: int = 8080) -> http.server.HTTPServer:
        """Start local HTTP server to handle OAuth callback."""
        def handler_factory(oauth_client):
            def create_handler(*args, **kwargs):
                return OAuthCallbackHandler(*args, oauth_client=oauth_client, **kwargs)
            return create_handler
        
        handler = handler_factory(self)
        server = http.server.HTTPServer(('localhost', port), handler)
        return server
    
    def authorize(self, open_browser: bool = True, timeout: int = 120) -> bool:
        """
        Perform OAuth authorization flow.
        
        Args:
            open_browser: Whether to automatically open browser
            timeout: Timeout in seconds for callback
            
        Returns:
            True if authorization successful, False otherwise
        """
        # Reset previous state
        self.auth_code = None
        self.callback_state = None
        self.auth_error = None
        
        # Parse redirect URI to get port
        parsed_uri = urllib.parse.urlparse(self.config.redirect_uri)
        port = parsed_uri.port or 8080
        
        # Start callback server
        server = self.start_callback_server(port)
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()
        
        try:
            # Get authorization URL and open browser
            auth_url = self.get_authorization_url()
            print(f"Authorization URL: {auth_url}")
            
            if open_browser:
                webbrowser.open(auth_url)
            else:
                print("Please open the above URL in your browser to authorize the application.")
            
            # Wait for callback
            start_time = time.time()
            while time.time() - start_time < timeout:
                if self.auth_code or self.auth_error:
                    break
                time.sleep(0.5)
            
            # Check results
            if self.auth_error:
                print(f"Authorization error: {self.auth_error}")
                return False
            
            if not self.auth_code:
                print("Authorization timeout - no callback received")
                return False
            
            # Verify state parameter
            if self.callback_state != self.state:
                print("State parameter mismatch - possible CSRF attack")
                return False
            
            print("Authorization code received successfully")
            return True
            
        finally:
            server.shutdown()
            server.server_close()
    
    def exchange_code_for_token(self) -> bool:
        """Exchange authorization code for access token."""
        if not self.auth_code or not self.code_verifier:
            print("No authorization code or code verifier available")
            return False
        
        # Prepare token request
        data = {
            'grant_type': 'authorization_code',
            'code': self.auth_code,
            'redirect_uri': self.config.redirect_uri,
            'client_id': self.config.client_id,
            'code_verifier': self.code_verifier
        }
        
        # Add client secret if provided (for confidential clients)
        if self.config.client_secret:
            data['client_secret'] = self.config.client_secret
        
        try:
            # Make token request
            encoded_data = urllib.parse.urlencode(data).encode('utf-8')
            request = urllib.request.Request(
                self.config.token_url,
                data=encoded_data,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            
            with urllib.request.urlopen(request) as response:
                response_data = json.loads(response.read().decode('utf-8'))
            
            # Extract tokens
            self.access_token = response_data.get('access_token')
            self.refresh_token = response_data.get('refresh_token')
            
            # Calculate expiration time
            expires_in = response_data.get('expires_in')
            if expires_in:
                self.token_expires_at = time.time() + int(expires_in)
            
            print("Access token obtained successfully")
            return True
            
        except urllib.error.HTTPError as e:
            error_response = e.read().decode('utf-8')
            print(f"Token exchange failed: {e.code} - {error_response}")
            return False
        except Exception as e:
            print(f"Token exchange error: {e}")
            return False
    
    def refresh_access_token(self) -> bool:
        """Refresh access token using refresh token."""
        if not self.refresh_token:
            print("No refresh token available")
            return False
        
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': self.config.client_id
        }
        
        if self.config.client_secret:
            data['client_secret'] = self.config.client_secret
        
        try:
            encoded_data = urllib.parse.urlencode(data).encode('utf-8')
            request = urllib.request.Request(
                self.config.token_url,
                data=encoded_data,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            
            with urllib.request.urlopen(request) as response:
                response_data = json.loads(response.read().decode('utf-8'))
            
            # Update tokens
            self.access_token = response_data.get('access_token')
            new_refresh_token = response_data.get('refresh_token')
            if new_refresh_token:
                self.refresh_token = new_refresh_token
            
            # Update expiration
            expires_in = response_data.get('expires_in')
            if expires_in:
                self.token_expires_at = time.time() + int(expires_in)
            
            print("Access token refreshed successfully")
            return True
            
        except Exception as e:
            print(f"Token refresh error: {e}")
            return False
    
    def is_token_expired(self) -> bool:
        """Check if access token is expired."""
        if not self.token_expires_at:
            return False
        # Add 5 minute buffer
        return time.time() >= (self.token_expires_at - 300)
    
    def get_valid_token(self) -> Optional[str]:
        """Get a valid access token, refreshing if necessary."""
        if not self.access_token:
            return None
        
        if self.is_token_expired() and self.refresh_token:
            if self.refresh_access_token():
                return self.access_token
            else:
                return None
        
        return self.access_token
    
    def make_authenticated_request(self, url: str, method: str = 'GET', 
                                 data: Optional[Dict[str, Any]] = None,
                                 headers: Optional[Dict[str, str]] = None) -> Optional[Dict[str, Any]]:
        """Make an authenticated HTTP request."""
        token = self.get_valid_token()
        if not token:
            print("No valid access token available")
            return None
        
        # Prepare headers
        request_headers = headers or {}
        request_headers['Authorization'] = f'Bearer {token}'
        
        try:
            # Prepare request
            request_data = None
            if data:
                if method.upper() in ['POST', 'PUT', 'PATCH']:
                    request_data = json.dumps(data).encode('utf-8')
                    request_headers['Content-Type'] = 'application/json'
            
            request = urllib.request.Request(url, data=request_data, headers=request_headers)
            request.get_method = lambda: method.upper()
            
            with urllib.request.urlopen(request) as response:
                return json.loads(response.read().decode('utf-8'))
                
        except urllib.error.HTTPError as e:
            print(f"HTTP error {e.code}: {e.read().decode('utf-8')}")
            return None
        except Exception as e:
            print(f"Request error: {e}")
            return None

# Common OAuth provider configurations
OAUTH_PROVIDERS = {
    'google': OAuthConfig(
        client_id='',  # Set your client ID
        authorization_url='https://accounts.google.com/o/oauth2/v2/auth',
        token_url='https://oauth2.googleapis.com/token',
        scope='openid email profile'
    ),
    'github': OAuthConfig(
        client_id='',  # Set your client ID
        authorization_url='https://github.com/login/oauth/authorize',
        token_url='https://github.com/login/oauth/access_token',
        scope='user:email'
    ),
    'microsoft': OAuthConfig(
        client_id='',  # Set your client ID
        authorization_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize',
        token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token',
        scope='openid email profile'
    )
}

def main():
    """Example usage of OAuth client."""
    print("OAuth Authentication Example")
    print("=" * 40)
    
    # Example with Google OAuth (you need to set client_id)
    config = OAUTH_PROVIDERS['google']
    if not config.client_id:
        print("Please set client_id in OAUTH_PROVIDERS['google'] to test")
        return
    
    client = OAuthClient(config)
    
    # Perform authorization
    print("Starting OAuth flow...")
    if client.authorize():
        print("Authorization successful!")
        
        # Exchange code for token
        if client.exchange_code_for_token():
            print("Token exchange successful!")
            print(f"Access token: {client.access_token[:20]}...")
            
            # Example API call
            user_info = client.make_authenticated_request('https://www.googleapis.com/oauth2/v2/userinfo')
            if user_info:
                print(f"User info: {user_info}")
        else:
            print("Token exchange failed")
    else:
        print("Authorization failed")

if __name__ == "__main__":
    main()