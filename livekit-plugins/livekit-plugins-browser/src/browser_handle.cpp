#include "browser_handle.hpp"

void BrowserHandle::SetSize(int width, int height) {
  width_ = width;
  height_ = height;

  if (browser_)
    browser_->GetHost()->WasResized();
}


void BrowserHandle::Close() {
  if (browser_)
    browser_->GetHost()->CloseBrowser(true);
}
// Modified on Tue Jan 21 11:33:40 PM +01 2025
// Modified on Tue Jan 21 11:33:48 PM +01 2025
// Modified on Tue Jan 21 11:33:48 PM +01 2025
