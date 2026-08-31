from enum import IntFlag

from pydantic import BaseModel


class DivingFishScope(IntFlag):
    PROFILE = 1
    PROBER_PROFILE_READ = 2
    PROBER_RECORDS_READ = 4
    PROBER_RECORDS_WRITE = 8
    CHUNITHM_RECORDS_READ = 16
    CHUNITHM_RECORDS_WRITE = 32


DIVINGFISH_SCOPE_NAMES = {
    DivingFishScope.PROFILE: "profile",
    DivingFishScope.PROBER_PROFILE_READ: "prober.profile.read",
    DivingFishScope.PROBER_RECORDS_READ: "prober.records.read",
    DivingFishScope.PROBER_RECORDS_WRITE: "prober.records.write",
    DivingFishScope.CHUNITHM_RECORDS_READ: "chunithm.records.read",
    DivingFishScope.CHUNITHM_RECORDS_WRITE: "chunithm.records.write",
}
DIVINGFISH_SCOPE_MASK = sum(scope.value for scope in DivingFishScope)


class DeviceAuthorization(BaseModel):
    """发起绑定后水鱼账号返回的授权信息"""

    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: str
    expires_in: int
    interval: int = 5
    #: 收尾方式。请求里带了 `handoff=code` 时水鱼会原样回显，
    #: 借此确认本次绑定确实要等用户回填确认码
    handoff: str = "poll"


class AccessToken(BaseModel):
    """代用户访问的令牌，没有 `refresh_token`，过期后重新换取"""

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    #: 该用户的水鱼用户 ID。只有兑换确认码的响应里有，换票的响应里没有
    sub: str | None = None
